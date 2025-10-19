// 引入 three.js 与 CSS3DRenderer （确保在 index.html 中加载对应库）
import * as THREE from 'three';
import { CSS3DObject } from 'three/examples/jsm/renderers/CSS3DRenderer.js';

/**
 * BookPage 类
 * 用于创建一本书中的单页对象
 * 包含：
 *   - 纸张三维模型（带牛皮纸纹理）
 *   - 覆盖在其上的 HTML 层，可自由添加文字、图片或嵌入页面
 *   - 支持自定义大小、内容、动画变形（折叠、弯曲等）
 */
export class BookPage {
  /**
   * 构造函数：创建书页对象
   * @param {Object} options                - 参数对象
   * @param {number} options.width=2        - 书页宽度（单位：Three.js 场景单位，约等于米）
   * @param {number} options.height=3       - 书页高度
   * @param {string} options.textureURL     - 牛皮纸背景贴图路径（默认在 /textures/paper.jpg）
   * @param {string} options.htmlContent='' - 要显示在书页上的 HTML 内容（如文字、图片等）
   * @param {THREE.Scene} options.scene     - three.js 场景对象，用于将书页添加进去
   */
  constructor({ width = 2, height = 3, textureURL = './textures/paper.jpg', htmlContent = '', scene }) {
    this.width = width;
    this.height = height;
    this.textureURL = textureURL;
    this.scene = scene;

    // 创建一个 Three.js 组（Group），用于同时控制纸张和 HTML 内容
    this.group = new THREE.Group();

    // === 1. 创建书页的三维网格 ===
    const geometry = new THREE.PlaneGeometry(width, height, 32, 32); // 细分网格方便后续做扭曲动画

    // 加载牛皮纸纹理
    const texture = new THREE.TextureLoader().load(textureURL);
    texture.wrapS = texture.wrapT = THREE.RepeatWrapping; // 允许重复纹理
    texture.repeat.set(1, 1);

    const material = new THREE.MeshPhongMaterial({
      map: texture,       // 纸张背景
      side: THREE.DoubleSide, // 双面可见
    });

    this.mesh = new THREE.Mesh(geometry, material);
    this.mesh.castShadow = true;   // 投射阴影
    this.mesh.receiveShadow = true; // 接收阴影
    this.group.add(this.mesh);

    // === 2. 创建 HTML 内容层（CSS3D） ===
    const contentDiv = document.createElement('div');
    contentDiv.className = 'page-content';
    contentDiv.style.width = `${width * 200}px`;  // 转换为像素
    contentDiv.style.height = `${height * 200}px`;
    contentDiv.style.pointerEvents = 'auto';      // 允许点击交互
    contentDiv.style.overflow = 'hidden';
    contentDiv.innerHTML = htmlContent;           // 插入自定义 HTML 内容

    // 创建 CSS3D 对象（Three.js 提供的类，可以让 HTML 与 3D 场景结合）
    this.htmlObject = new CSS3DObject(contentDiv);
    this.htmlObject.scale.set(0.005, 0.005, 0.005); // 缩小比例（因为 HTML 默认太大）
    this.group.add(this.htmlObject);

    // === 3. 添加进场景 ===
    if (scene) scene.add(this.group);
  }

  /**
   * 设置页面内容
   * @param {string} htmlString - HTML 字符串（图片、文字、div等）
   */
  setContent(htmlString) {
    this.htmlObject.element.innerHTML = htmlString;
  }

  /**
   * 对页面执行形变（例如弯曲、折叠）
   * @param {Function} deformFn - 接受 (x, y) 坐标并返回 z 偏移的函数
   *   例如： (x, y) => 0.1 * Math.sin(x * Math.PI)
   */
  applyDeformation(deformFn) {
    const position = this.mesh.geometry.attributes.position;
    const original = position.array;
    const vertexCount = position.count;

    for (let i = 0; i < vertexCount; i++) {
      const x = position.getX(i);
      const y = position.getY(i);
      const z = deformFn(x / this.width, y / this.height); // 归一化坐标
      position.setZ(i, z);
    }

    position.needsUpdate = true; // 通知 Three.js 更新顶点
    this.mesh.geometry.computeVertexNormals(); // 更新法线以保持光照正确
  }

  /**
   * 每帧更新（如果有动画）
   * 可在主循环中调用： page.update()
   */
  update() {
    // HTML 内容层位置同步（通常无需修改，CSS3DRenderer 会自动跟随相机）
  }

  /**
   * 设置书页在三维空间中的位置
   * @param {number} x
   * @param {number} y
   * @param {number} z
   */
  setPosition(x, y, z) {
    this.group.position.set(x, y, z);
  }

  /**
   * 设置书页旋转角度（单位：弧度）
   * @param {number} rx 绕X轴旋转
   * @param {number} ry 绕Y轴旋转
   * @param {number} rz 绕Z轴旋转
   */
  setRotation(rx, ry, rz) {
    this.group.rotation.set(rx, ry, rz);
  }
}
